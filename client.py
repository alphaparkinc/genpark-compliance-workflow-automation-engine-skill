class ComplianceWorkflowAutomationEngineClient:
    def verify_compliance(self, document_payload: dict, regulatory_framework: str = "ISO-27001") -> dict:
        violations = []
        if not document_payload.get("encryption"):
            violations.append({"code": "ERR_NO_ENCRYPTION", "msg": "Missing data-at-rest encryption specification"})
        return {
            "compliance_status": "COMPLIANT" if not violations else "NON_COMPLIANT",
            "violations": violations
        }
