use qt5qml::core::{QString, ToQString};

include!(concat!(env!("OUT_DIR"), "/qffi_ExampleObject.rs"));

pub struct ExampleObjectPrivate {
    qobject: *mut ExampleObject,
    property: Option<String>,
}

impl ExampleObjectPrivate {
    pub fn new(qobject: *mut ExampleObject) -> Self {
        Self {
            qobject,
            property: None,
        }
    }

    pub fn property(&self) -> QString {
        self.property.to_qstring()
    }

    pub fn set_property(&mut self, value: &QString) {
        self.property = Some(value.to_string());
        unsafe { &mut *self.qobject }.propertyChanged(value);
    }
}
