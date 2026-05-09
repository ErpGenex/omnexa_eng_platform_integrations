### Omnexa Eng Platform Integrations

CDE / integration stubs. Depends on `omnexa_engineering_consulting`; `consulting_bridge.get_cde_upload()` forwards to `cde_upload` until integrations are split out.

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app omnexa_eng_platform_integrations
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/omnexa_eng_platform_integrations
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
