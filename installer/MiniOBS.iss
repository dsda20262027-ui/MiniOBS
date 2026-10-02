#define MyAppName "Mini OBS Studio"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Mini OBS"
#define MyAppExeName "MiniOBS.exe"

[Setup]
AppId={{B7A4D2F7-2D9E-4B0D-8F0C-4C7C1D8E7A11}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\MiniOBS
DefaultGroupName={#MyAppName}
OutputDir=output
OutputBaseFilename=MiniOBS-Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
ArchitecturesInstallIn64BitMode=x64compatible
UninstallDisplayName={#MyAppName}
PrivilegesRequired=admin

[Files]
Source: "..\build\MiniOBS.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\Mini OBS Studio"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\Mini OBS Studio"; Filename: "{app}\{#MyAppExeName}"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Запустить Mini OBS Studio"; Flags: nowait postinstall skipifsilent
