use qobject_compiler::moc::MocConfig;
use qobject_compiler::{CcBuild, QObjectBuild, QObjectMethod, QObjectProp, QObjectSignal, TypeRef};
use qt5qml::core::QString;

fn main() {
    // Qt
    let core = pkg_config::probe_library("Qt5Core").unwrap();
    let qml = pkg_config::probe_library("Qt5Qml").unwrap();

    let mut moc = MocConfig::new();
    let mut cpp = CcBuild::new();
    cpp.flag("-std=gnu++11");
    for include in &core.include_paths {
        cpp.include(include);
        moc.include_path(include);
    }
    for include in &qml.include_paths {
        cpp.include(include);
        moc.include_path(include);
    }

    QObjectBuild::new("ExampleObject")
        .inherit(TypeRef::qobject())
        .property(
            QObjectProp::new::<QString>("property")
                .read("property")
                .write("setProperty")
                .notify("propertyChanged"),
        )
        .method(QObjectMethod::new("property").ret::<QString>())
        .method(QObjectMethod::new("setProperty").arg::<&QString>("value"))
        .signal(QObjectSignal::new("propertyChanged").arg::<&QString>("value"))
        .qml(true)
        .build(&cpp, &moc);
}
