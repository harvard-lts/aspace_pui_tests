ASpace PUI tests, currently designed to be run against a running instance of ASpace using our data subset developed by Alex Duryee as part of the aspace ugprade to 3.0.2.

To Run Tests:
1. Clone repository
2. Copy `env.example` to `.env`. Replace base URL with the base URL for the aspace pui
2. Run `docker-compose -f docker-compose.yml up --build`

Automated tests based on Julie Wetherill's aspace PUI testing spreadsheet here:
https://docs.google.com/spreadsheets/d/19m0FpJyDCU-YRZwuvspJrOjMPFVNF49_U4vX6P_OtfA/edit#gid=0

To-Dos:
- Add a package for reading pdfs in order to test spreadsheet contents (currently only check successful download)

Tests from spreadsheet that were unable to be added:
- All instances of comparing record counts against prod record counts are not relevant due to the intentionally much-smaller size of the data subset.