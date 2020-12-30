# Rust example application for Sailfish OS

![Build](https://github.com/R1tschY/harbour-rust-example/workflows/Build/badge.svg)

It is based on the default Sailfish example application for C++. The example uses my `qobject-compiler` project to create an example QObject class. The `sailfishapp` crate is currently needed to integrate with Sailfish. For a more complex example please look at https://github.com/R1tschY/harbour-sailify.

The project contains a QtCreator dummy project so it can be imported to QtCreator. QtCreator can then be used as QML editor.

# Build

    sfdk build
    sfdk deploy


# Known issues

* does not compile on i486 (Sailfish SDK seems to not support this platform for Rust)
