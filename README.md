# idlynx-nyt
An action to provision your daily NYT subscription provided by Idaho Lynx Libraries

## Configuring to run for your account

- Fork it!
- Enable Actions on the fork
- Enable the scheduled workflow in Actions
- Add secrets with values with:
  - `NYT_USERNAME`, your nytimes.com login
  - `NYT_PASSWORD`, your nytimes.com password
  - `LIBRARY_CARD_NUMBER`, your Idaho Lynx Consortium library card number
- Add a _variable_ with a value:
  - `LIBRARY_NAME`, your canonical library name, defaults to Meridan Library District if not provided.  See https://form.jotform.com/220755446894164 for available values.
- Profit!