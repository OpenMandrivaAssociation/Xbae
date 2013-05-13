%define srcname	xbae

%define major		4
%define libname		%mklibname %name %major
%define develname	%mklibname %name -d

Summary:	Xbae Widget Set
Name:		Xbae
Version:	4.60.4
Release:	6
License:	BSD
Group:		System/Libraries
Url:		http://xbae.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/xbae/%srcname-%version.tar.gz
BuildRequires:	pkgconfig(x11)
BuildRequires:	lesstif-devel
BuildRequires:	pkgconfig(xt)
BuildRequires:	libxp-devel
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xpm)
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
Provides:       %{name}-devel = %{EVRD}
Provides:       lib%{name}-devel = %{EVRD}
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
%makeinstall_std

rm -rf %{buildroot}/%_prefix/Xbae

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_mandir}/man3/*
%_datadir/Xbae

%files -n %libname
%_libdir/*.so.*

%files -n %develname
%doc doc/*.html
%_includedir/%{name}
%_libdir/*.so


%changelog
* Sun Feb 21 2010 Funda Wang <fwang@mandriva.org> 4.60.4-4mdv2010.1
+ Revision: 508927
- simplify spec file

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 4.60.4-3mdv2009.0
+ Revision: 242970
- rebuild
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Jul 20 2007 Adam Williamson <awilliamson@mandriva.org> 4.60.4-1mdv2008.0
+ Revision: 54026
- rebuild against new lesstif
- move docs out of lib package to devel package
- move out of /usr/X11R6
- new devel policy
- drop pointless manual provide in lib package
- spec clean
- new release 4.60.4
- Import Xbae




* Tue Mar 21 2006 Lenny Cartier <lenny@mandriva.com> 4.60.2-1mdk
- 4.60.2

* Thu May 12 2005 Olivier Thauvin <nanardon@mandriva.org> 4.60.0-1mdk
- 4.60.0

* Tue Dec 07 2004 Lenny Cartier <lenny@mandrakesoft.com> 4.50.99-1mdk
- 4.50.99

* Sat Nov 15 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.9.11-4mdk 
- move man files in separate package
- fix provides
- Franck Villaume <fvill@freesurf.fr>
  - more buildrequires : groff-for-man

* Sat Apr 26 2003 Lenny Cartier <lenny@mandrakesoft.com> 4.9.11-3mdk
- adjust buildrequires

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 4.9.11-2mdk
- rebuild

* Thu Oct 03 2002 Lenny Cartier <lenny@mandrakesoft.com> 4.9.11-1mdk
- libification
- from Austin Acton <aacton@yorku.ca> :
	- initial package for Mandrake 9.0
