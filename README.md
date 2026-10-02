# Mini OBS Studio

Отдельный проект Mini OBS Studio с Windows-сборкой через GitHub Actions и установщиком Inno Setup.

## Что собирается автоматически

После каждого push в `main` GitHub Actions запускает Windows-сборку и создаёт два артефакта:

- `MiniOBS-Windows-Installer` — установщик `MiniOBS-Setup.exe` для установки в `C:\\Program Files\\MiniOBS`.
- `MiniOBS-Windows-EXE` — готовый `MiniOBS.exe` без установщика.

Сборку также можно запустить вручную: **Actions → Build MiniOBS for Windows → Run workflow**.

## Локальная сборка

Если нужно собрать на своём ПК, запусти `build.bat`, а затем собери `installer\\MiniOBS.iss` через Inno Setup.

## Важно

Текущая версия — интерфейсный прототип Mini OBS Studio. Кнопки интерфейса работают, но настоящий захват экрана/окна/микрофона и кодирование видео пока не подключены. Следующий этап можно сделать с реальной записью экрана, аудио, сценами, горячими клавишами и FFmpeg.
