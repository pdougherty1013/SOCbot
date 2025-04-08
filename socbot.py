import random
import time

class SOCBot:
    def __init__(self):
        self.name = "SOCBot"
        self.version = "0.1"
        self.commands = {
            "!help": self.show_help,
            "!alert": self.generate_alert,
            "!analyze": self.analyze_alert,
            "!about": self.about
        }

    def show_help(self):
        print("\nAvailable commands:")
        for command in self.commands:
            print(f"  {command}")
        print("  !exit - Exit the bot\n")

    def generate_alert(self):
        alerts = [
            "Suspicious login from Russia on port 22",
            "Malware signature detected on endpoint 192.168.1.45",
            "Excessive failed logins on admin account",
            "Possible phishing email reported by user",
            "Firewall detected port scanning attempt"
        ]
        alert = random.choice(alerts)
        print(f"\n[ALERT] {alert}\n")

    def analyze_alert(self):
        responses = [
            "Initiating threat intel lookup...",
            "Running sandbox analysis...",
            "Checking SIEM logs...",
            "Alert triaged as low priority. No action needed.",
            "False positive identified. Marking as benign."
        ]
        print(f"\n{random.choice(responses)}\n")

    def about(self):
        print(f"\n{self.name} v{self.version} — Your virtual SOC sidekick. \nTrained in memes, malware, and mission-critical alerts.\n")

    def run(self):
        print(f"Welcome to {self.name} v{self.version}! Type !help for commands.")
        while True:
            command = input("\n> ").strip().lower()
            if command == "!exit":
                print("\nGoodbye. Stay secure out there.\n")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("\n[ERROR] Unknown command. Type !help for a list of commands.\n")

if __name__ == "__main__":
    bot = SOCBot()
    bot.run()
