from app.providers.telephony.base import TelephonyProvider


class LiveKitSIPStubProvider(TelephonyProvider):
    def initiate_call(self, to_number: str, from_number: str) -> dict:
        return {
            "provider": "livekit-sip-stub",
            "status": "stubbed",
            "to_number": to_number,
            "from_number": from_number,
            "note": "PSTN/SIP trunk connectivity is not implemented yet.",
        }

    def end_call(self, call_id: str) -> dict:
        return {
            "provider": "livekit-sip-stub",
            "status": "stubbed",
            "call_id": call_id,
            "note": "No live call teardown in scaffold mode.",
        }
