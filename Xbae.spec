%define srcname	xbae

%define major 4
%define libname %mklibname %name %major
%define develname %mklibname %name -d

Summary:	Xbae Widget Set
Name:		Xbae
Version:	4.60.4
Release:	7
License:	BSD
Group:		System/Libraries
Url:		http://xbae.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/xbae/%srcname-%version.tar.gz
BuildRequires:	pkgconfig(x11)
BuildRequires:	lesstif-devel
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xp)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xpm)
Requires:		%{libname} = %{EVRD}

%description
XbaeMatrix is a free Motif table widget (also compatible with the free LessTif)
which presents an editable array of string data to the user in a scrollable 
table similar to a spreadsheet. The rows and columns of the Matrix may 
optionally be labelled. A number of "fixed" and "trailing fixed" rows or
columns may be specified.

%package -n %{libname}
Summary:	Xbae Widget Set
Group:		System/Libraries

%description -n %libname
XbaeMatrix is a free Motif table widget (also compatible with the free LessTif)
which presents an editable array of string data to the user in a scrollable
table similar to a spreadsheet. The rows and columns of the Matrix may
optionally be labelled. A number of "fixed" and "trailing fixed" rows or 
columns may be specified. 

%package -n %{develname}
Summary:		Development tools for programs which will use the %name library
Group:			Development/Other
Requires:		%{libname} = %{EVRD}
Provides:		%{name}-devel = %{EVRD}
Provides:		lib%{name}-devel = %{EVRD}
Obsoletes:		%{mklibname Xbae 4 -d}

%description -n %{develname}
The %{name}-devel package includes the header files and static libraries
necessary for developing programs using the %name library.

If you are going to develop programs which will use this library
you should install %{name}-devel.  You'll also need to have the %name
package installed.

%prep
%setup -q -n %srcname-%version

%build
%configure \
	--enable-shared \
    --disable-static \
    --disable-debug

%make

%install
%makeinstall_std

rm -rf %{buildroot}/%_prefix/Xbae

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_mandir}/man3/*
%{_datadir}/Xbae

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc doc/*.html
%{_includedir}/%{name}
%{_libdir}/*.so
