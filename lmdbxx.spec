Name: lmdbxx
Version: 1.0.0
Release: 1%{?dist}

License: Public Domain
Summary: C++ wrapper for the LMDB embedded B+ tree database library
URL: https://github.com/hoytech/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Requires: lmdb-devel
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix}

%files devel
%doc README.md FUNCTIONS.rst AUTHORS CREDITS VERSION
%license UNLICENSE
%{_includedir}/lmdb++.h

%changelog
* Thu Apr 22 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-1
- Updated to version 1.0.0.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14.1-7.20160229git0b43ca8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14.1-6.20160229git0b43ca8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14.1-5.20160229git0b43ca8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14.1-4.20160229git0b43ca8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14.1-3.20160229git0b43ca8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14.1-2.20160229git0b43ca8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.9.14.1-1.20160229git0b43ca8
- Initial SPEC release.
