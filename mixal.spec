Name:		mixal
Version:	1.08
Release:	3
Source0:	http://locke.ccil.org:/pub/esr/%{name}_%{version}.orig.tar.gz
Copyright:	distributable
Patch0:		%{name}_1.08-7.diff.gz
Group:		Development/Languages
Summary:	load-and-go assembler for Donald Knuth's MIX language
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Mixal is an assembler and interpreter for Donald Knuth's mythical MIX
computer, defined in: Donald Knuth, "The Art of Computer Programming",
Vol. 1: Fundamental Algorithms_. Addison-Wesley, 1973 (2nd ed.)

%prep
%setup -q -n %{name}-%{version}.orig
%patch -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}%{_bindir}/
install -d ${RPM_BUILD_ROOT}%{_mandir}/man1/
install mixal ${RPM_BUILD_ROOT}%{_bindir}/mixal
install mixal.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/mixal.1

%files
%defattr(644,root,root,755)
%doc READ.ME NOTES
%doc %{_mandir}/man1/
%attr(755,root,root) %{_bindir}/mixal

%clean
rm -rf $RPM_BUILD_ROOT
