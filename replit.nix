{ pkgs }: {
  deps = [
    pkgs.gdb
    pkgs.nodejs-16_x
    pkgs.replitPackages.prybar-python310
    pkgs.replitPackages.stderred
  ];
}