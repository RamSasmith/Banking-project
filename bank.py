import json
from pathlib import Path
from account import SavingsAccount, CurrentAccount

FILE = Path("data/bank.json")

class Bank:
    def __init__(self):
        FILE.parent.mkdir(exist_ok=True)
        if not FILE.exists():
            self.save({"customers": [], "accounts": [], "transactions": []})

    def load(self):
        return json.loads(FILE.read_text())

    def save(self, data):
        FILE.write_text(json.dumps(data, indent=2))

    def create(self, form):
        data = self.load()
        number = "AC" + str(1001 + len(data["accounts"]))
        keys = ("name", "dob", "gender", "aadhar", "pan", "email",
                "phone", "address", "account_type")
        customer = {key: form[key] for key in keys}
        account = {"number": number, "customer": customer,
                   "type": form["account_type"], "balance": 0}
        data["customers"].append(customer)
        data["accounts"].append(account)
        self.save(data)
        return number

    def find(self, number, data):
        for account in data["accounts"]:
            if account["number"] == number:
                return account
        raise ValueError("Account not found")

    def action(self, number, amount, action):
        data = self.load()
        acc = self.find(number, data)
        cls = SavingsAccount if acc["type"] == "Savings" else CurrentAccount
        obj = cls(number, acc["customer"], acc["type"], acc["balance"])
        getattr(obj, action.lower())(amount)
        acc["balance"] = obj.balance
        data["transactions"].append(
            {"account": number, "action": action, "amount": float(amount)})
        self.save(data)

    def dashboard(self):
        data = self.load()
        return {"accounts": data["accounts"],
                "transactions": data["transactions"],
                "total": sum(a["balance"] for a in data["accounts"])}
