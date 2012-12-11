%define name	pngrewrite
%define version	1.3.0
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Graphics
Source0:	%{name}-%{version}.tar.bz2
URL:		http://entropymine.com/jason/pngrewrite/
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary:	PNG size optimizer
BuildRequires:	png-devel

%description
Pngrewrite is little utility that reduces the unnecessarily large
palettes that too many programs write into PNG files. It also
optimizes transparency settings, and reduces the bits-per-pixel
if possible. Handy for post-processing images before putting them
on a web site. 

%prep
%setup -q

%build
%{__cc} $RPM_OPT_FLAGS -lpng -o %{name} %{name}.c

%install
rm -rf $RPM_BUILD_ROOT
install -m755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdv2011.0
+ Revision: 614600
- the mass rebuild of 2010.1 packages

* Thu Mar 11 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.3.0-1mdv2010.1
+ Revision: 518214
- update to 1.3.0

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.2.1-7mdv2010.0
+ Revision: 430750
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.2.1-6mdv2009.0
+ Revision: 259129
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.2.1-5mdv2009.0
+ Revision: 247043
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.2.1-3mdv2008.1
+ Revision: 136426
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import pngrewrite


* Fri Jun 30 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.2.1-3mdv2007.0
- rebuild

* Tue Feb 08 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2.1-2mdk
- reuild

* Sat Jan 10 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2.1-1mdk
- initial mdk release
