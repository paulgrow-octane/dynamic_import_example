This is a minimal example demonstrating how:

1.  modules can be dynamically loaded within a namespace
2.  how specific functions within these dynamically imported modules may be mapped to names within the same namespace

The directory structure of this repo is as follows:

```
├── main.py
└── module_a
    ├── __init__.py
    ├── create_bar_table.py
    └── create_foo_table.py
```

`module_a` contains two functions: `create_bar_table` and `create_foo_table`. However, the name `create_bar_table` _is the function_ `module_a.create_bar_table.execute`.

The implications of such an approach are that simply adding another `create_{name}_table.py` file will **automatically** be made available when importing `module_a` with no further boilerplate
