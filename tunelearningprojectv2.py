class TuneLearningApp:
    def __init__(self):
        self.learnt_tunes = {}
        self.current_tunes = {}
        self.current_wl = set()

    def number_tunes(self):
        if len(self.learnt_tunes) == 1:
            print("You've learnt 1 tune")
        else:
            print("You've learnt %d tunes" % len(self.learnt_tunes))
        self.first_action()

    def see_learnt_tunes(self):
        print(self.learnt_tunes)
        self.first_action()
    
    def tune_to_learnt(self):
        tune = self.get_user_input("Enter a tune you've learnt\n")
        if tune in self.learnt_tunes:
            print("You've already learnt this tune")
        elif tune in self.current_tunes and tune in self.current_wl:
            self.learnt_tunes[tune] = self.current_tunes[tune]
            del self.current_tunes[tune]
            del self.current_wl[tune]
        elif tune in self.current_tunes:
            self.learnt_tunes[tune] = self.current_tunes[tune]
            del self.current_tunes[tune]
        elif tune in self.current_wl:
            self.learnt_tunes[tune] = self.current_wl[tune]
            del self.current_wl[tune]
        else:
            categories = self.get_categories()
            self.learnt_tunes[tune] = categories
        while True:
            more_tunes_decision = self.get_user_input("Do you want to enter more tunes? (Enter 'yes' or 'no'): ")
            if more_tunes_decision.lower() == "yes":
                self.tune_to_learnt()
            elif more_tunes_decision.lower() == "no":
                self.first_action()
            else:
                print("Please enter 'yes' or 'no'")
        
            
    def start_tune(self):
        name = self.get_user_input("Enter the name of the tune you'd like to start:")
        if name in self.learnt_tunes:
            print(f"The tune '{name}' is already in the list.")
            return

        categories = self.get_categories()
        self.current_tunes[name] = categories

        while True:
            decision = self.get_user_input("Enter 'home' to go back or 'continue' to start a new tune:")
            if decision.lower() == 'home':
                self.first_action()
                break
            elif decision.lower() == 'continue':
                self.start_tune()
                break
            else:
                print("Please enter 'home' or 'continue'.")

    def get_user_input(self, prompt):
        return input(prompt).strip()

    def get_categories(self):
        outer_loop_flag = True
        categories = set()
        while outer_loop_flag:
            category_input = self.get_user_input(
                f"Enter any categories this tune falls under:\nList of existing categories: {categories}\n"
            )
            categories.add(category_input)
            while True:
                new_category_decision = self.get_user_input("Do you want to enter more categories? (Enter 'yes' or 'no'): ")
                if new_category_decision.lower() == "no":
                    outer_loop_flag = False
                    break
                elif new_category_decision.lower() == "yes":
                    break
                else:
                    print("Please enter 'yes' or 'no'")

        return categories

    def see_current(self):
        print(self.current_tunes)
        self.first_action()

    def add_tune_to_wishlist(self):
        tune = self.get_user_input("Enter a tune you'd like to add to your wishlist:")
        categories = self.get_categories()
        categories_tuple = tuple(categories)
        self.current_wl.add((tune, categories_tuple))
        while True:
            decision = self.get_user_input("Enter 'home' to go back or 'continue' to add a tune to your wishlist:")
            if decision.lower() == 'home':
                self.first_action()
                break
            elif decision.lower() == 'continue':
                self.start_tune()
                break
            else:
                print("Please enter 'home' or 'continue'.")


    def see_wl(self):
        for tune, categories in self.current_wl:
            print(f"Tune: {tune}, Categories: {categories}")
        self.first_action()

    def first_action(self):
        command = self.get_user_input("""Please enter a command:
# of learnt tunes
See learnt tunes                                     
Add tune to learnt tunes
Start new tune
See current tunes
Add tune to wishlist
See wishlist
At any point type "back" to return to the previous prompt, or "home" to return to this screen
""")
        if command.lower() in ["# of learnt tunes", "# learnt tunes", "# learnt"]:
            self.number_tunes()
        elif command.lower() in ["see learnt tunes", "see learnt"]:
            self.see_learnt_tunes()
        elif command.lower() in ["add tune to learnt", "add tune to learnt tunes", "tune to learnt", "add learnt"]:
            self.tune_to_learnt()
        elif command.lower() in ["start new tune", "new tune", "start tune"]:
            self.start_tune()
        elif command.lower() in ["see current tunes", "current tunes", "see tunes"]:
            self.see_current()
        elif command.lower() == "add tune to wishlist":
            self.add_tune_to_wishlist()
        elif command.lower() == "see wishlist":
            self.see_wl()
        else:
            print("Please enter a valid command")
            self.first_action()

    def run(self):
        self.first_action()

if __name__ == "__main__":
    app = TuneLearningApp()
    app.run()