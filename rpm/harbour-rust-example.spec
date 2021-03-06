Name:       harbour-rust-example
Summary:    Rust example application for Sailfish OS
Version:    1.0
Release:    1
Group:      Qt/Qt
License:    LICENSE
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils
BuildRequires:  rust
BuildRequires:  cargo


%description
A example for a Rust application for Sailfish OS.

# - PREP -----------------------------------------------------------------------
%prep
%setup -q -n %{name}-%{version}

# - BUILD ----------------------------------------------------------------------
%build

export RPM_VERSION=%{version}
export RUSTFLAGS="-Clink-arg=-Wl,-z,relro,-z,now -Ccodegen-units=1 -Clink-arg=-rdynamic"

# release
export CARGO_INCREMENTAL=0
cargo build --release --target-dir=target --locked --manifest-path %{_sourcedir}/../Cargo.toml

# Make build with Qt Creator work
touch Makefile

# debug
#cargo build --target-dir=target --locked --manifest-path %{_sourcedir}/../Cargo.toml

# - INSTALL --------------------------------------------------------------------
%install

rm -rf %{buildroot}
install -d %{buildroot}%{_datadir}/%{name}

install -Dm 755 target/release/%{name} -t %{buildroot}%{_bindir}

install -Dm 644 %{_sourcedir}/../%{name}.png -t %{buildroot}%{_datadir}/icons/hicolor/86x86/apps
install -Dm 644 %{_sourcedir}/../%{name}.desktop -t %{buildroot}%{_datadir}/applications
cp -r %{_sourcedir}/../qml %{buildroot}%{_datadir}/%{name}/qml

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop
   
# - CHECK ----------------------------------------------------------------------
%check

# check that main symbol exists
if nm -D target/release/%{name} | grep "T main$" > /dev/null ; then
  echo "main symbol exists"
else
  echo "main symbol is missing"
  exit 1
fi


# - FILES ----------------------------------------------------------------------
%files

%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}/qml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/86x86/apps/%{name}.png


