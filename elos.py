from __future__ import annotations

import argparse
import json

from elos_core import elos_identity, elos_status


def main() -> int:
    parser = argparse.ArgumentParser(prog="elos", description="ELOS CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("whoami", help="Pokaż tożsamość Elosa")
    sub.add_parser("status", help="Pokaż status Elosa (JSON)")

    args = parser.parse_args()

    if args.cmd == "status":
        print(json.dumps(elos_status(), ensure_ascii=False, indent=2))
        return 0

    # domyślnie: whoami
    print(elos_identity())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
