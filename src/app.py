#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Application launcher for tinyApps.
"""

from __future__ import annotations

from components import oneSpotApp


class Blueprint:
    """Application launcher."""

    @staticmethod
    def run() -> None:
        """Display menu and launch selected application."""

        apps = {
            "1": ("oneSpotApp", oneSpotApp.oneSpotApp.mainApp),
        }

        print("Available tinyApps:")
        for key, (name, _) in apps.items():
            print(f"{key}. {name}")

        choice = input("\nSelect an application: ").strip()

        if choice not in apps:
            print("Invalid selection.")
            return

        app_name, app_factory = apps[choice]

        try:
            print(f"\nLaunching {app_name}...")
            app = app_factory()
            app.mainloop()

        except Exception as exc:
            print(f"Failed to launch {app_name}: {exc}")


if __name__ == "__main__":
    Blueprint.run()
