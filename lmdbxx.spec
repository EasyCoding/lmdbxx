%global commit0 0b43ca87d8cfabba392dfe884eb1edb83874de02
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20160229

Name: lmdbxx
Summary: C++ wrapper for the LMDB embedded B+ tree database library
Version: 0.9.14.1
Release: 0.1.%{date}git%{shortcommit0}%{?dist}

License: Public Domain
URL: https://github.com/bendiken/%{name}
Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
BuildArch: noarch

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{commit0}

%build
doxygen

%install
mkdir -p %{buildroot}%{_includedir}
install -m 0644 -p lmdb++.h %{buildroot}%{_includedir}

%files devel
%doc README.rst AUTHORS CREDITS
%license UNLICENSE
%{_includedir}/lmdb++.h

%changelog
* Wed Jul 04 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.9.14.1-0.1.20160229git0b43ca8
- Initial SPEC release.
