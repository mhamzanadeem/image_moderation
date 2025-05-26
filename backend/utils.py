def dummy_moderation(image_bytes):
    # Simulate classification
    return {
        "nudity": {"confidence": 0.1},
        "violence": {"confidence": 0.7},
        "hate_symbol": {"confidence": 0.05},
        "self_harm": {"confidence": 0.0}
    }
