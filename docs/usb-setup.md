# USB setup

Copy this repository to a dedicated USB drive.

## Windows

Run `scripts/Windows/collect-report.bat`.

## Linux

Run:

```bash
bash scripts/Linux/collect-report.sh
```

Then open `dashboard/index.html` in a browser and choose **Import JSON reports**.

## Privacy precautions

- Do not put passwords, private keys, API tokens, or other secrets in reports.
- Treat reports as sensitive infrastructure information.
- Encrypt the USB drive when it contains real environment data.
- Do not enable autorun or automatic execution.
- Only collect information from systems you own or are authorized to administer.
- The dashboard has no external JavaScript or CSS dependencies and does not need Internet access.
