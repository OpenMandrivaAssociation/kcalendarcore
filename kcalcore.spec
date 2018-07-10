%define major 5
%define libname %mklibname KF5CalendarCore %{major}
%define devname %mklibname KF5CalendarCore -d

Name: kcalcore
Version:	 18.04.3
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for handling calendar data
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: bison
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(libical)
Obsoletes: %{mklibname akonadi-calendar 4}
Obsoletes: %{mklibname kcalcore 4}
Obsoletes: %{mklibname akonadi-kcal 4}
Obsoletes: %{mklibname kcal 4}

%description
KDE library for handling calendar data

%package -n %{libname}
Summary: KDE library for handling calendar data
Group: System/Libraries

%description -n %{libname}
KDE library for handling calendar data

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_sysconfdir}/xdg/kcalcore.categories
%{_sysconfdir}/xdg/kcalcore.renamecategories
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
