from google.cloud import firestore

db = firestore.Client.from_service_account_json("firebase_credentials.json")


def add_metadata(collection: str, data: dict):
    doc_ref = db.collection(collection).add(data)
    return doc_ref[1].id


def get_metadata(collection: str, doc_id: str):
    doc_ref = db.collection(collection).document(doc_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        raise Exception("Document not found")


def fetch_all_documents(collection: str):
    """Fetches all documents in a Firestore collection."""
    docs = db.collection(collection).stream()
    return [{doc.id: doc.to_dict()} for doc in docs]
