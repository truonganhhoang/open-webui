from open_webui.utils.misc import parse_ollama_modelfile


def test_parse_base_model_with_special_chars():
    model_text = """FROM phi3:mini-4k-instruct
PARAMETER temperature 0.7
"""
    info = parse_ollama_modelfile(model_text)
    assert info["base_model_id"] == "phi3:mini-4k-instruct"
    assert info["params"]["temperature"] == 0.7

