# Image-provider routing

This repository separates **visual reasoning** from **image rendering**. The A/U/C/M specs, prompt, locked layout, review criteria, and run artifacts are model-independent. The final renderer is selected through a local JSON record:

```text
user-config/image-generation-provider.json
```

The record is Git-ignored. It contains no API key, only the provider route, model identifier, optional endpoint, and the names of environment variables that a host agent/client must read at execution time.

## Configure in one command

```bash
python3 scripts/configure_image_provider.py list
python3 scripts/configure_image_provider.py use agent-native
python3 scripts/configure_image_provider.py use openai-images-api --model <model-id>
python3 scripts/configure_image_provider.py use comfyui-http --model <workflow-or-model-id> --base-url http://127.0.0.1:8188
python3 scripts/configure_image_provider.py show
python3 scripts/configure_image_provider.py clear
```

The current catalog is in `image-provider-presets.json`. Provider presets deliberately do not hard-code fast-changing model names; pass the model ID that your account and client currently support.

## Contract for every agent

1. Read `user-config/image-generation-provider.json` before final rendering when it exists.
2. Generate only from the compiled prompt and locked output spec. The chosen provider cannot relax A/U/C/M extraction, direct-reference rules, layout locks, or review requirements.
3. Use the selected route if the agent has an appropriate native tool, authorized API client, or local endpoint. Read credentials from the configured environment variable at execution time; never write, echo, commit, or put a credential in the JSON file.
4. If the route cannot be executed in the current agent, preserve the prompt and all audit artifacts, explain the missing capability, and ask the user to select another route or execute it in a compatible agent. Do not silently switch providers.
5. Treat `custom-http` and local endpoints as user-authorized integrations. Do not probe arbitrary endpoints or upload raw references without explicit authorization.

## Configuration schema

```json
{
  "schema_version": 1,
  "provider_id": "openai-images-api",
  "display_name": "OpenAI-style Images API",
  "execution": "openai-images-api",
  "model": "your-current-model-id",
  "api_key_env": "OPENAI_API_KEY",
  "base_url_env": "OPENAI_BASE_URL",
  "base_url": null,
  "notes": "Supply the current provider-supported image model ID at configuration time."
}
```

Use `agent-native` when the host already exposes a configured image-generation tool. It intentionally has no credential or fixed model ID; the host's own selected image model remains the renderer.
