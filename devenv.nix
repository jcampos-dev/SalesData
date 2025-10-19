{ pkgs, lib, config, inputs, ... }:

{
  packages = with pkgs; [
    python313Packages.flake8
    black
    basedpyright
  ];

  languages = {
    nix.enable = true;
    python = {
      enable = true;
      venv.enable = true;
      uv = {
        enable = true;
        sync.enable = true;
      };
    };
  };
}
