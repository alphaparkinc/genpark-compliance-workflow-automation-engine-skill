from client import ComplianceWorkflowAutomationEngineClient

def main():
    client = ComplianceWorkflowAutomationEngineClient()
    res = client.verify_compliance({"project": "Fintech API", "encryption": True}, "SEC-FIN-2026")
    print(f"Status: {res['compliance_status']}")
    print(f"Violations Count: {len(res['violations'])}")

if __name__ == "__main__":
    main()
