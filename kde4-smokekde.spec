%define         _state          stable
%define         orgname         smokekde
%define         qtver           4.8.0

Summary:	smokekde - A SMOKE library
Summary(pl.UTF-8):	smokekde - Biblioteka SMOKE
Name:		kde4-smokekde
Version:	4.8.4
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	4fb01d0ceea8e142cdea8b8049e6b2ac
URL:		http://www.kde.org/
BuildRequires:	akonadi-devel
BuildRequires:	attica-devel
BuildRequires:	kde4-kate-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	kde4-okular-devel >= %{version}
BuildRequires:	kde4-smokeqt-devel >= %{version}
BuildRequires:	soprano-devel
Obsoletes:	kde4-kdebindings-smoke-kde < 4.6.99
Obsoletes:	smokekde <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SMOKE library (Scripting Meta Object Kompiler Engine).

%description -l pl.UTF-8
Biblioteka SMOKE (Scripting Meta Object Kompiler Engine - silnik
kompilatora metaobiektów skryptowych).

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-smokeqt-devel >= %{version}
Obsoletes:	kde4-kdebinings-smoke-devel < 4.6.99
Obsoletes:	smokekde-devel <= 4.8.0

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/libsmoke*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmoke*.so.?

%files devel
%defattr(644,root,root,755)
%{_includedir}/smoke/*.h
%{_datadir}/smokegen/kde-config.xml
%attr(755,root,root) %{_libdir}/libsmoke*.so
