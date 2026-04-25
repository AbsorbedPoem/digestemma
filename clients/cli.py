import json
from typing import Any
from lib.vars import assitant_host

import httpx
import typer


def _extract_text(payload: Any) -> str:
    if isinstance(payload, str):
        return payload

    if isinstance(payload, dict):
        for key in ("message", "content", "response", "text"):
            value = payload.get(key)
            if isinstance(value, str) and value.strip():
                return value
            if isinstance(value, dict):
                nested = _extract_text(value)
                if nested:
                    return nested

        return json.dumps(payload, ensure_ascii=True, indent=2)

    return str(payload)


def _request_chat(
    client: httpx.Client,
    prompt: str,
) -> str:
    body: dict[str, Any] = {"prompt": prompt}

    response = client.post('/chat/', params=body)
    response.raise_for_status()

    content_type = response.headers.get("content-type", "")
    if "application/json" in content_type:
        return _extract_text(response.json())

    return response.text.strip()


def main() -> None:
    typer.echo(f"Connected to {assitant_host}. Type 'exit' or 'quit' to stop.")

    try:
        with httpx.Client(base_url=assitant_host, timeout=None) as client:
            while True:
                prompt = typer.prompt(">>>").strip()
                if not prompt:
                    continue
                if prompt.lower() in {"exit", "quit"}:
                    break

                try:
                    reply = _request_chat(client, prompt)
                except httpx.HTTPStatusError as exc:
                    typer.echo(
                        f"API error {exc.response.status_code}: {exc.response.text}",
                        err=True,
                    )
                    continue
                except httpx.HTTPError as exc:
                    typer.echo(f"Connection error: {exc}", err=True)
                    raise typer.Exit(code=1)

                typer.echo(f"\n{reply}\n")
    except KeyboardInterrupt:
        typer.echo("\nBye.")


if __name__ == "__main__":
    typer.run(main)
