import whisper
model = whisper.load_model("base")

def trans(link_to_file):
    result = model.transcribe(link_to_file)
    print (result["text"])
    return result["text"]
