# s1000d-examples

Self-made example data for S1000D Issue 7. The Zenn book "[S1000D実践](https://zenn.dev/shuji_bonji/books/s1000d-practice)" (Japanese) uses these files. Japanese README: [README.ja.md](./README.ja.md)

> [!IMPORTANT]
> This is not an official S1000D sample. The author made the data for a fictional ticket vending machine (model identification code `KENBAIKI`). The repository does not contain the S1000D specification, the XML schemas, or the official Bike samples.

## Folders

| Folder | Content |
| --- | --- |
| `kenbaiki/csdb/` | The CSDB of the ticket vending machine: 18 XML files (16 data modules, 1 publication module, 1 comment) and 6 ICN files (5 PNG figures, 1 STEP model) |
| `kenbaiki/icn-src/` | Scripts that made the ICN files (HTML + headless Chrome for the PNG files, CadQuery for the STEP file) |
| `kenbaiki/chapters/` | Files that each chapter of the book adds or changes |

The files in `chapters/08-xsd/` and `chapters/09-brex/` contain errors on purpose. Copy the files in `chapters/10-create/` to `chapters/14-csdb/` over `kenbaiki/csdb/` to get the CSDB after all the examples of the book.

## Verification record

Checked on 2026-11-22 (JST) with `verify_csdb` of s1000d-verify-mcp ([S1000D Stack](https://github.com/shuji-bonji/s1000d-stack)), the S1000D Issue 7 schemas and the default BREX.

| Target | DMs and PMs | XSD | BREX | References |
| --- | --- | --- | --- | --- |
| `kenbaiki/csdb/` | 17 | 17 valid | 17 passed (0 violations) | 0 unresolved |
| CSDB with the chapter files | 23 | 23 valid | 23 passed (0 violations) | 0 unresolved |

The result shows only that the tools found no errors in the items they check. It does not certify conformance to S1000D.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Credit "shuji-bonji" and the URL of this repository.
