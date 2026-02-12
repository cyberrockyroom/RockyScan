from rockyscan.utils.banner import show_banner
from rockyscan.menu import show_menu
from rockyscan.launcher import launch

def main():
    show_banner()
    while True:
        choice = show_menu()
        if choice == "0":
            break
        launch(choice)

if __name__ == "__main__":
    main()
