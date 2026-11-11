from models.test_case import TestCase
from services.test_case_register import TestCaseRegister


class TestCaseDialog:
    def __init__(self):
        self._register = TestCaseRegister()  


    def run(self):
        while True:
            
            print("\n--- Testfallsregister ---")
            print("1. Registrera testfall")
            print("2. Visa testfall")
            print("0. Avsluta")

            

            choice = input("Välj ett alternativ: ")

            if choice == "1":
                self.create_test_case()
            elif choice == "2":
                self.list_test_cases()
            elif choice == "0":
                print("Programmet avslutas.") 
                break
            else:
                print("Ogiltigt val. Försök igen.")   

    def create_test_case(self):
        title = input("Ange testfallets titel: ")
        description = input("Beskriv testfallet: ")
        expected_result = input("Ange förväntat resultat: ")

        test_case = TestCase(title, description, expected_result)
        self._register.add_test_case(test_case)

        print("Testfallet har registrerats!") 


    def list_test_cases(self):
        test_cases = self._register.get_all_test_cases()

        if not test_cases:
          print("Det finns inga registrerade testfall.")
          return

        for test_case in test_cases:
            print("\nTitel:", test_case.title)
            print("Beskrivning:", test_case.description)
            print("Förväntat resultat:", test_case.expected_result)