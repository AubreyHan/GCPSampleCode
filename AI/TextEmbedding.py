from vertexai.language_models import TextEmbeddingModel
import vertexai

vertexai.init(project='hy-auth-001')

def text_embedding() -> list:
    """Text embedding with a Large Language Model."""
    model = TextEmbeddingModel.from_pretrained("textembedding-gecko@001")
    embeddings = model.get_embeddings(["What is life?"])
    for embedding in embeddings:
        vector = embedding.values
        print(f"Length of Embedding Vector: {len(vector)}")

text_embedding()