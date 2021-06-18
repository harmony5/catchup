# Catchup 📝

CLI app to manage to-do's. Made with 💖 in 🐍.

## Features 🧰

- List all saved to-do's (`show`).
- Filter to-do's by status (`show --status STATUS`).
- `add` to-do's.
- Mark to-do's as `complete`.
- `remove` to-do's from the list.

## Installation 📦⬇

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install it.

```bash
pip install catchup
```

## Usage 🛠

To add a new to-do to the list:

```bash
$ catchup add "This is a new to-do."
Saved new to-do to the Database: This is a new to-do.

$ catchup add "This is another to-do."
Saved new to-do to the Database: This is another to-do.
```

To get a list of all saved to-do's:

```bash
$ catchup show
  id  description             status       timestamp
----  ----------------------  -----------  --------------------------
   1  This is a new to-do.    Completed    2021-06-01 12:00:00.000000
   2  This is another to-do.  In Progress  2021-06-01 12:01:20.000000
```

If you want to filter by status:

```bash
$ catchup show --status "in progress"
  id  description             status       timestamp
----  ----------------------  -----------  --------------------------
   2  This is another to-do.  In Progress  2021-06-01 12:01:20.000000

$ catchup show --status complete
  id  description             status       timestamp
----  ----------------------  -----------  --------------------------
   1  This is a new to-do.    Completed    2021-06-01 12:00:00.000000
```

With the `complete` subcommand, you can mark a to-do as completed, specified by its `id`:

```bash
$ catchup complete 2
Todo with id #1 was marked as completed.

$ catchup show
  id  description             status       timestamp
----  ----------------------  -----------  --------------------------
   1  This is a new to-do.    Completed    2021-06-01 12:00:00.000000
   2  This is another to-do.  Completed    2021-06-01 12:01:20.000000
```

And if you want to completely remove a to-do from the list:

```bash
$ catchup remove 2
Removed to-do with id #2.

$ catchup show
  id  description             status       timestamp
----  ----------------------  -----------  --------------------------
   1  This is a new to-do.    Completed    2021-06-01 12:00:00.000000
```

## Contributing ✍

Pull requests are welcome. For major changes, [bug fixes](https://github.com/harmony5/catchup/issues/new?template=bug_report.md&labels=bug&projects=harmony5%2Fcatchup%2F1) or [feature requests](https://github.com/harmony5/catchup/issues/new?template=feature_request.md&labels=bug&projects=harmony5%2Fcatchup%2F1), please open an issue first to discuss what you would like to change.

## License 📜⚖

This project uses the [MIT](https://choosealicense.com/licenses/mit) license.
