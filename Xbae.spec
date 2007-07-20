%define name Xbae
%define version 4.60.2
%define release %mkrel 1

%define major 4
%define libname %mklibname %name %major
%define libnamedev %mklibname %name %major -d

Summary:   Xbae Widget Set
Name:      %name
Version:   %version
Release:   %release
License: BSD
Group:     System/Libraries
Url:	   http://xbae.sourceforge.net/
Source:    ftp://ftp.hungry.com/pub/hungry/lesstif/xbae-%version.tar.bz2
BuildRoot: %{_tmppath}/%name-root
BuildRequires: lesstif-devel libxpm-devel XFree86-devel glibc-static-devel groff-for-man
Requires: %libname = %version

%description
XbaeMatrix is a free Motif table widget (also compatible with the free LessTif) 
which presents an editable array of string data to the user in a scrollable 
table similar to a spreadsheet. The rows and columns of the Matrix may 
optionally be labelled. A number of "fixed" and "trailing fixed" rows or
columns may be specified.

%package -n %libname
Summary:   Xbae Widget Set
Group:     System/Libraries
Provides:  lib%{name} = %version-%release

%description -n %libname
XbaeMatrix is a free Motif table widget (also compatible with the free LessTif)
which presents an editable array of string data to the user in a scrollable
table similar to a spreadsheet. The rows and columns of the Matrix may
optionally be labelled. A number of "fixed" and "trailing fixed" rows or 
columns may be specified. 

%package -n %libnamedev
Summary:        Development tools for programs which will use the %name library
Group:          Development/Other
Requires:       %libname = %{version}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}

%description -n %libnamedev
The %name-devel package includes the header files and static libraries
necessary for developing programs using the %name library.

If you are going to develop programs which will use this library
you should install %name-devel.  You'll also need to have the %name
package installed.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n xbae-%version

%build
export LESSTIFTOP=$PWD

export CFLAGS="$RPM_OPT_FLAGS"
%configure \
	--libdir=%_prefix/X11R6/%_lib \
	--prefix=/usr/X11R6 --enable-shared --disable-static --disable-debug

%make

%install
%makeinstall

mkdir -p $RPM_BUILD_ROOT/usr/X11R6
mv $RPM_BUILD_ROOT/usr/%{_lib} $RPM_BUILD_ROOT/usr/X11R6
mv $RPM_BUILD_ROOT/usr/include $RPM_BUILD_ROOT/usr/X11R6

rm -rf $RPM_BUILD_ROOT/%_prefix/Xbae

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_mandir}/man3/*
%_datadir/Xbae

%files -n %libname
%defattr (-,root,root)
%doc doc/*.html
/usr/X11R6/%_lib/*.so.*

%files -n %libnamedev
%defattr (-,root,root)
/usr/X11R6/include/Xbae/*
/usr/X11R6/%_lib/*.so
/usr/X11R6/%_lib/*.la
