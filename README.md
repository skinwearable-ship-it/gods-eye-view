# God's Eye View

An open-source, offline-first security situational-awareness dashboard for computers and networks you own or are authorized to administer.

## What it does

- Shows a single dashboard for imported endpoint reports.
- Collects a small, transparent set of local system/network facts with an explicit command.
- Works without third-party web CDNs or cloud telemetry.
- Can be carried on a USB drive.
- Keeps data local: reports are JSON files you choose to import.

## What it does not do

- No keylogging, credential harvesting, screen capture, webcam/microphone access, or covert persistence.
- No automatic execution when a USB drive is inserted.
- No scanning of arbitrary remote networks.
- No hidden upload of telemetry.

## USB layout

```
gods-eye-view/
├── dashboard/
│   └── index.html
├── agent/
│   └── collect.py
├── scripts/
│   ├── Windows/
│   │   └── collect-report.bat
│   └── Linux/
│       └── collect-report.sh
├── docs/
│   └── usb-setup.md
├── LICENSE
└── README.md
```

## Quick start

1. Copy/clone this repository to a USB drive.
2. On a computer you own or administer, run the platform-specific collector.
3. Open `dashboard/index.html` locally.
4. Import one or more generated `report-*.json` files.
5. Review the dashboard and keep the reports only where appropriate.

The collector uses Python 3 and the standard library only.

## Security model

The dashboard is intentionally static and offline. A report is treated as untrusted input and rendered as text; it is not executed.

For stronger privacy, encrypt your USB drive and do not store reports containing sensitive infrastructure information on shared computers.

## License

MIT.
