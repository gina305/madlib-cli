# madlib-cli

## Feature Requirements:

* Create and test a read_template function that takes in a path to text file and returns a stripped string of the file’s contents.
** read_template should raise a FileNotFoundError if path is invalid.
* Create and test a parse_template function that takes in a template string and returns a string with language parts removed and a separate tuple of those language parts.
* Create and test a merge function that takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.
