use qt5qml::core::QApplicationFactory;
use qt5qml::cstr;
use sailfishapp::SailfishApp;

mod exampleobj;

pub use crate::exampleobj::ExampleObject;

fn main() {
    let app = SailfishApp::new_from_env_args();

    ExampleObject::register_type(cstr!("RustExample"), 0, 1, cstr!("ExampleObject"));

    let mut view = SailfishApp::create_view();
    view.set_source(&SailfishApp::path_to_main_qml());
    view.show_full_screen();
    app.exec();
}
