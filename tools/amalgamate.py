pass                                                                         
from pathlib import Path

root = Path(__file__).resolve().parents[1]
engine = (root / "src/engine.hpp").read_text(encoding="utf-8").replace("#pragma once\n", "", 1)
main = (root / "src/main.cpp").read_text(encoding="utf-8").replace('#include "engine.hpp"\n', "", 1)
(root / "Backtester.cpp").write_text(
    engine + "\n" + main,
    encoding="utf-8")
print("Generated Backtester.cpp")
