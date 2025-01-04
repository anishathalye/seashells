# Development

Seashells uses the [Hatch] project manager ([installation instructions][hatch-install]).

[Hatch]: https://hatch.pypa.io/
[hatch-install]: https://hatch.pypa.io/latest/install/

## Formatting and linting

You can run the [Ruff][ruff] formatter and linter with:

```bash
hatch fmt
```

This will automatically make [safe fixes][fix-safety] to your code. If you want to only check your files without making modifications, run `hatch fmt --check`.

[ruff]: https://github.com/astral-sh/ruff
[fix-safety]: https://docs.astral.sh/ruff/linter/#fix-safety

## Packaging

You can use [`hatch build`][hatch-build] to create build artifacts, a [source distribution ("sdist")][sdist] and a [built distribution ("wheel")][bdist].

You can use [`hatch publish`][hatch-publish] to publish build artifacts to [PyPI][pypi].

[hatch-build]: https://hatch.pypa.io/latest/build/
[sdist]: https://packaging.python.org/en/latest/glossary/#term-Source-Distribution-or-sdist
[bdist]: https://packaging.python.org/en/latest/glossary/#term-Built-Distribution
[hatch-publish]: https://hatch.pypa.io/latest/publish/
[pypi]: https://pypi.org/

## Continuous integration

Formatting/linting is [checked in CI][ci].

[ci]: .github/workflows/ci.yml
