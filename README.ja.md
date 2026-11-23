# s1000d-examples

S1000D Issue 7 の書き方を確かめるための、自作の例のデータです。Zenn Book「[S1000D実践 — データモジュールを読み、確かめ、作る](https://zenn.dev/shuji_bonji/books/s1000d-practice)」の各章が、このリポジトリのファイルを使っています。

> [!IMPORTANT]
> このリポジトリのデータは、S1000D の公式サンプルではありません。架空の指定席券売機（モデル識別コード `KENBAIKI`）を題材に、著者が作ったものです。S1000D の仕様書、XML スキーマ、公式サンプル（Bike Samples）は含みません。

## フォルダー

| フォルダー | 内容 |
| --- | --- |
| `kenbaiki/csdb/` | 券売機の CSDB です。XML のファイルが 18 個（DM 16、パブリケーションモジュール 1、コメント 1）と、図のファイル（ICN）が 6 個あります |
| `kenbaiki/icn-src/` | 図のファイルを作ったスクリプトです |
| `kenbaiki/chapters/` | 本の章ごとに、足したファイルと直したファイルです |

`kenbaiki/chapters/` の中身は次のとおりです。

| フォルダー | 章 | 内容 |
| --- | --- | --- |
| `08-xsd/` | XSD で検証する | わざと誤りを 2 つ入れた DM（`invalid-example.xml`）。XSD の検証でエラーが 2 件出ます |
| `09-brex/` | BREX で検査する | わざと値を 2 つ変えた DM（`brex-violation-example.xml`）。プロジェクトの BREX への違反が 2 件出ます |
| `10-create/` | DM を作る | 下書きから作った説明の DM（きっぷの払い戻し） |
| `11-revise/` | DM を直し、改版する | 「到着駅を選ぶ」の作業中の版（`001-01`） |
| `12-applicability/` | 適用性 | ACT、PCT と、適用性を足した DM の作業中の版が 2 つ |
| `13-publication/` | PM でまとめる | 10 章で作った DM を目次に足したパブリケーションモジュール |
| `14-csdb/` | CSDB をフォルダーと Git で持つ | データ管理リスト（DML）。突き合わせの結果を見せるために、CSDB と食い違う行を 2 つ入れています |

`08-xsd/` と `09-brex/` のファイルは、検査で誤りが見つかることを確かめるためのものです。S1000D のファイル名にしていないのは、CSDB のファイルと取り違えないためです。

`10-create/` から `14-csdb/` のファイルを `kenbaiki/csdb/` のファイルに重ねて 1 つのフォルダーに置くと、本の例をすべて行った後の CSDB になります。`13-publication/` のパブリケーションモジュールは、`kenbaiki/csdb/` の同じ名前のファイルを置き換えます。

## 検証の記録

2026-11-22（JST）に、[S1000D Stack](https://github.com/shuji-bonji/s1000d-stack) の s1000d-verify-mcp の `verify_csdb` で、S1000D Issue 7 のスキーマと既定 BREX を使って確かめた結果です。

| 対象 | DM・PM の数 | XSD | BREX | 参照 |
| --- | --- | --- | --- | --- |
| `kenbaiki/csdb/` | 17 | 17 件が `valid` | 17 件が `passed`（違反 0 件） | 指す先の無い参照は 0 件 |
| 章のファイルを重ねた CSDB | 23 | 23 件が `valid` | 23 件が `passed`（違反 0 件） | 指す先の無い参照は 0 件 |

BREX の検査は、DM とパブリケーションモジュールでは 3 層（券売機のプロジェクトの BREX、組織の BREX、S1000D の既定 BREX）で行われます。

## 図のファイル（ICN）

| ファイル | 内容 | 作り方 |
| --- | --- | --- |
| `ICN-K0001-00001-001-01.PNG` 〜 `00004` | 券売機の画面（トップ、到着駅の選択、支払い、残高不足） | HTML と CSS で描き、Chrome のヘッドレスモードで PNG にしました（`icn-src/gen.py`） |
| `ICN-K0001-00005-001-01.PNG` | 前面扉の取っ手の図 | SVG で描き、同じ方法で PNG にしました |
| `ICN-K0001-00006-001-01.STEP` | 筐体、前面扉、取っ手の 3D のモデル | CadQuery 2.8.0（Open CASCADE）で作りました（`icn-src/model.py`） |

画面と駅の名前は架空のものです。

> [!NOTE]
> DM は、3D のモデルの形式を、仕様パッケージの `notations.xml` にある名前 `step`（公開識別子は「STEP AP203 3D Models Encoding」）で宣言しています。CadQuery が書き出したファイルのスキーマは AP214 です。AP203 での書き出しは、試した範囲ではできませんでした。

> [!NOTE]
> コメント（`COM-KENBAIKI-K0001-2026-00001-Q`）の指摘 R-1・R-2 は、図のファイルを入れる前のレビューの記録です。

> [!WARNING]
> 検証の結果は、道具が調べた範囲で誤りが見つからなかったことを示すだけです。S1000D に準拠していることの保証ではありません。BREX には、人が読んで確かめるルールもあります。

## ライセンス

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja) です。出典（著者名 shuji-bonji と、このリポジトリの URL）を示せば、複製、改変、再配布ができます。
