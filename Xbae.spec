%define name 	Xbae
%define srcname	xbae
%define version	4.60.4
%define release	%mkrel 4

%define major		4
%define libname		%mklibname %name %major
%define develname	%mklibname %name -d

Summary:	Xbae Widget Set
Name:		%name
Version:	%version
Release:	%release
License:	BSD
Group:		System/Libraries
Url:		http://xbae.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/xbae/%srcname-%version.tar.gz
BuildRoot:	%{_tmppath}/%name-root
BuildRequires:	libx11-devel
BuildRequires:	lesstif-devel
BuildRequires:	libxt-devel
BuildRequires:	libxp-devel
BuildRequires:	libxmu-devel
BuildRequires:	libxpm-devel
Requires:	%libname = %version

%description
XbaeMatrix is a free Motif table widget (also compatible with the free LessTif)
which presents an editable array of string data to the user in a scrollable 
table similar to a spreadsheet. The rows and columns of the Matrix may 
optionally be labelled. A number of "fixed" and "trailing fixed" rows or
columns may be specified.

%package -n %libname
Summary:   Xbae Widget Set
Group:     System/Libraries

%description -n %libname
XbaeMatrix is a free Motif table widget (also compatible with the free LessTif)
which presents an editable array of string data to the user in a scrollable
table similar to a spreadsheet. The rows and columns of the Matrix may
optionally be labelled. A number of "fixed" and "trailing fixed" rows or 
columns may be specified. 

%package -n %develname
Summary:        Development tools for programs which will use the %name library
Group:          Development/Other
Requires:       %libname = %{version}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname Xbae 4 -d}

%description -n %develname
The %name-devel package includes the header files and static libraries
necessary for developing programs using the %name library.

If you are going to develop programs which will use this library
you should install %name-devel.  You'll also need to have the %name
package installed.

%prep
%setup -q -n %srcname-%version

%build
%configure2_5x --enable-shared --disable-static --disable-debug
%make

%install
rm -fr %buildroot
%makeinstall_std

rm -rf $RPM_BUILD_ROOT/%_prefix/Xbae

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_mandir}/man3/*
%_datadir/Xbae

%files -n %libname
%defattr (-,root,root)
%_libdir/*.so.*

%files -n %develname
%defattr (-,root,root)
%doc doc/*.html
%_includedir/%{name}
%_libdir/*.so
%_libdir/*.la
