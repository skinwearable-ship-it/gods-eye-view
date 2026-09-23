#!/usr/bin/env python3
"""God's Eye View local collector.

Collects a minimal, transparent snapshot of the machine on which it runs.
It does not upload data, install persistence, capture credentials, or scan
remote hosts.
"""
from __future__ import annotations
import json, platform, socket, subprocess, time
from datetime import datetime, timezone
from pathlib import Path

def run(cmd: list[str]) -> str:
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=3, check=False)
        return (p.stdout or "").strip()
    except (OSError, subprocess.SubprocessError):
        return ""

def default_gateway() -> str:
    system = platform.system().lower()
    if system == "windows":
        out = run(["route", "print", "0.0.0.0"])
        for line in out.splitlines():
            parts = line.split()
            if len(parts) >= 4 and parts[0] == "0.0.0.0":
                return parts[2]
    elif system == "linux":
        for line in run(["ip", "route", "show", "default"]).splitlines():
            parts = line.split()
            if len(parts) >= 3 and parts[:2] == ["default", "via"]:
                return parts[2]
    elif system == "darwin":
        for line in run(["route", "-n", "get", "default"]).splitlines():
            if line.strip().startswith("gateway:"):
                return line.split(":", 1)[1].strip()
    return ""

def local_ip() -> str:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(1)
            s.connect(("192.0.2.1", 80))
            return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"

def dns_servers() -> list[str]:
    system = platform.system().lower()
    if system == "linux":
        try:
            lines = Path("/etc/resolv.conf").read_text(errors="ignore").splitlines()
            return [x.split()[1] for x in lines if x.startswith("nameserver ")][:4]
        except OSError:
            return []
    if system == "windows":
        result = []
        for line in run(["ipconfig", "/all"]).splitlines():
            s = line.strip()
            if "DNS Servers" in s and ":" in s:
                value = s.split(":", 1)[1].strip()
                if value: result.append(value)
            elif result and ":" not in s and s and len(result) < 4:
                if s[0].isdigit() or ":" in s: result.append(s)
        return result[:4]
    return []

def uptime_seconds():
    try:
        txt = Path("/proc/uptime").read_text().split()[0]
        return int(float(txt))
    except (OSError, IndexError, ValueError):
        return None

def main() -> None:
    now = datetime.now(timezone.utc)
    host = socket.gethostname() or "unknown-host"
    report = {
        "schema":"gods-eye-view/v1",
        "id":f"{host}-{int(time.time())}",
        "collected_at":now.isoformat(),
        "hostname":host,
        "os":platform.platform(),
        "python":platform.python_version(),
        "architecture":platform.machine(),
        "uptime_seconds":uptime_seconds(),
        "network":{"local_ip":local_ip(),"gateway":default_gateway(),"dns":dns_servers()},
        "notes":"Collected locally. No data was uploaded by this tool."
    }
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    path = Path.cwd()/f"report-{stamp}.json"
    path.write_text(json.dumps(report, indent=2)+"
", encoding="utf-8")
    print(f"Wrote {path}")

if __name__=="__main__":
    main()
