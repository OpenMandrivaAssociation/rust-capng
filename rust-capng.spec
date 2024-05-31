# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
%bcond_without check
%global debug_package %{nil}

%global crate capng

Name:           rust-capng
Version:        0.2.3
Release:        1
Summary:        Rust wrapper for libcap-ng
Group:          Development/Rust

License:        Apache-2.0 OR BSD-3-Clause
URL:            https://crates.io/crates/capng
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  (crate(bitflags/default) >= 1.0.0 with crate(bitflags/default) < 2.0.0~)
BuildRequires:  (crate(libc/default) >= 0.2.69 with crate(libc/default) < 0.3.0~)

%global _description %{expand:
Rust wrapper for libcap-ng.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(capng) = 0.2.3
Requires:       (crate(bitflags/default) >= 1.0.0 with crate(bitflags/default) < 2.0.0~)
Requires:       (crate(libc/default) >= 0.2.69 with crate(libc/default) < 0.3.0~)
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-BSD-3-Clause
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(capng/default) = 0.2.3
Requires:       cargo
Requires:       crate(capng) = 0.2.3

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
