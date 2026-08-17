import sys

from PySide6.QtWidgets import QApplication

from ui.hud import ZIDHUD


def main():
    app = QApplication(sys.argv)

    app.setApplicationName("ZID AI")

    window = ZIDHUD()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()