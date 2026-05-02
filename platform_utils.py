import os
import sys


def get_ollama_executable():
    """Return the best path to the local bundled `ollama` executable.

    Priority:
    1. Bundled executable in the repository `./ollama/ollama(.exe)`
    2. Fallback to executable name `ollama` (assumes in PATH)
    """
    base = os.path.abspath(os.path.dirname(__file__))
    # Windows uses .exe
    if sys.platform.startswith("win"):
        candidate = os.path.join(base, "ollama", "ollama.exe")
    else:
        candidate = os.path.join(base, "ollama", "ollama")

    if os.path.exists(candidate):
        # ensure executable bit on non-Windows
        try:
            if not sys.platform.startswith("win"):
                st = os.stat(candidate).st_mode
                # add owner execute bit
                os.chmod(candidate, st | 0o100)
        except Exception:
            pass
        return candidate

    # fallback to relying on PATH
    return "ollama"
