{ pkgs }: {
  deps = [
    pkgs.python311Packages.pytest
    pkgs.cowsay
  ];
}