import subprocess
from pathlib import Path


ARQUIVO_AUDIO = "request_audio.wav"


def gravar_audio(duracao=5, arquivo=ARQUIVO_AUDIO):
    print(f"Ouvindo... gravando por {duracao} segundos.")

    comando = [
        "ffmpeg",
        "-y",
        "-f", "pulse",
        "-i", "default",
        "-t", str(duracao),
        "-ac", "1",
        "-ar", "16000",
        arquivo,
    ]

    resultado = subprocess.run(
        comando,
        capture_output=True,
        text=True
    )

    if resultado.returncode != 0:
        print("Erro ao gravar com ffmpeg:")
        print(resultado.stderr)
        raise RuntimeError("Falha ao gravar áudio.")

    caminho = Path(arquivo).resolve()
    print(f"Áudio salvo em: {caminho}")
    return str(caminho)


if __name__ == "__main__":
    gravar_audio(5)