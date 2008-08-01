%define name	pngrewrite
%define version	1.2.1
%define release	%mkrel 6

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

