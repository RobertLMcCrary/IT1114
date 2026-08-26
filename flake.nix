{
  description = "IT1114 - Simple Python Dev Flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

    devshell = {
      url = "github:numtide/devshell";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    { nixpkgs, devshell, ... }:
    let
      systems = [
        "aarch64-darwin"
        "aarch64-linux"
        "x86_64-darwin"
        "x86_64-linux"
      ];

      eachSystem =
        f:
        nixpkgs.lib.genAttrs systems (
          system:
          f {
            inherit system;
            pkgs = nixpkgs.legacyPackages.${system};
          }
        );
    in
    {
      devShells = eachSystem (
        { pkgs, system, ... }:
        let
          python = pkgs.python312.withPackages (
            ps: with ps; [
              pygame
              numpy
              requests
              pytest
              black
              ruff
            ]
          );
        in
        {
          default = (devshell.legacyPackages.${system}.mkShell) {
            name = "IT1114";

            packages = [
              python
            ];

            commands = [
              {
                name = "run";
                category = "app";
                help = "Run main.py";
                command = "python main.py \"$@\"";
              }
              {
                name = "repl";
                category = "app";
                help = "Start a Python REPL with project packages available";
                command = "python";
              }
              {
                name = "fmt";
                category = "quality";
                help = "Format Python with black";
                command = "black .";
              }
              {
                name = "lint";
                category = "quality";
                help = "Lint Python with ruff";
                command = "ruff check .";
              }
              {
                name = "test";
                category = "quality";
                help = "Run tests with pytest";
                command = "pytest";
              }
            ];
          };
        }
      );

      formatter = eachSystem ({ pkgs, ... }: pkgs.nixfmt);
    };
}
